import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import random, csv, time

PAD = 6

def clamp(x, a, b): return max(a, min(b, x))

# 단순 공정 모델(교육용)
# 최적: T≈180°C, v≈40개/분, H≈45%
def defect_rate_pct(T, v, H):
    # 온도/속도는 이차 패널티, 습도는 55% 이상에서 선형 패널티
    pT = ((T - 180.0) / 15.0)**2
    pv = ((v - 40.0) / 10.0)**2
    pH = max(0.0, (H - 55.0) / 15.0)
    base = 1.5
    rate = base + 7.0*pT + 5.0*pv + 4.0*pH
    return float(clamp(rate, 0.0, 100.0))
