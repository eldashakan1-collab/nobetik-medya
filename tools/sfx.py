"""Telifsiz ses efekti katmanı üretir (tamamen sentez, örnek ses kullanılmaz).

Kullanım: python3 tools/sfx.py cue.json out.wav
cue.json: {"duration": 30, "events": [{"t": 1.0, "type": "tick"}, ...],
           "ambient": [[0, 11.5], [13.6, 30]]}
Türler: tick, beep, beep_fast, bell, freeze, chime, whoosh, pop, buzz
"""
import json
import sys
import wave

import numpy as np

SR = 44100


def env(n, a=0.005, r=0.08):
    e = np.ones(n)
    na, nr = int(a * SR), int(r * SR)
    if na: e[:na] = np.linspace(0, 1, na)
    if nr: e[-nr:] *= np.linspace(1, 0, nr)
    return e


def tone(f, d, vol=0.3, a=0.005, r=0.08, harm=(1,)):
    t = np.arange(int(d * SR)) / SR
    s = sum(np.sin(2 * np.pi * f * h * t) / (i + 1) for i, h in enumerate(harm))
    return vol * s * env(len(t), a, r)


def noise(d, vol=0.1, lp=0.02):
    n = np.random.default_rng(3).standard_normal(int(d * SR))
    y = np.zeros_like(n); acc = 0.0
    for i, v in enumerate(n):
        acc += lp * (v - acc); y[i] = acc
    return vol * y / (np.abs(y).max() + 1e-9)


def sound(kind):
    if kind == "tick":
        return tone(3200, 0.03, 0.18, 0.001, 0.025) + noise(0.03, 0.05, 0.5)
    if kind == "beep":
        return tone(1000, 0.09, 0.12, 0.003, 0.03)
    if kind == "beep_fast":
        return tone(1180, 0.07, 0.13, 0.003, 0.02)
    if kind == "bell":
        return np.concatenate([tone(880, 0.22, 0.16, 0.004, 0.18, (1, 2, 3)), tone(660, 0.35, 0.16, 0.004, 0.3, (1, 2, 3))])
    if kind == "freeze":
        return tone(55, 1.2, 0.35, 0.01, 1.0, (1, 2))
    if kind == "chime":
        return sum(tone(f, 2.2, 0.08, 0.05, 1.8) for f in (523.25, 659.25, 783.99, 1046.5))
    if kind == "whoosh":
        n = noise(0.6, 0.25, 0.15); return n * np.hanning(len(n))
    if kind == "pop":
        a = tone(600, 0.08, 0.2, 0.001, 0.07); b = tone(900, 0.05, 0.1, 0.001, 0.04)
        a[: len(b)] += b
        return a
    if kind == "buzz":
        return tone(140, 0.25, 0.12, 0.005, 0.1, (1, 2, 3, 4))
    raise ValueError(kind)


def main(cue_path, out):
    cue = json.load(open(cue_path))
    N = int(cue["duration"] * SR)
    mix = np.zeros(N)
    room = noise(cue["duration"], 0.035, 0.01) + tone(60, cue["duration"], 0.012, 0.5, 0.5)
    mask = np.zeros(N)
    for a, b in cue.get("ambient", []):
        ia, ib = int(a * SR), int(b * SR)
        fade = int(0.3 * SR)
        mask[ia:ib] = 1
        mask[ia:ia + fade] = np.linspace(0, 1, min(fade, ib - ia))
        mask[max(ib - fade, ia):ib] *= np.linspace(1, 0, ib - max(ib - fade, ia))
    mix += room * mask
    for ev in cue["events"]:
        s = sound(ev["type"]) * ev.get("gain", 1.0)
        i = int(ev["t"] * SR)
        j = min(N, i + len(s))
        mix[i:j] += s[: j - i]
    mix = mix / max(1.0, np.abs(mix).max() / 0.9)
    st = np.stack([mix, mix], 1)
    with wave.open(out, "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((st * 32767).astype("<i2").tobytes())


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
