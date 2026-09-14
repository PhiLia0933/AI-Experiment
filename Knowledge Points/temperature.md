# 大模型参数：温度（Temperature）

## 中文版

**是什么**：温度是控制大模型输出随机性的参数，像“随机性 / 创造力旋钮”。

**作用**：
- 低温：输出更确定、稳定、保守，适合事实问答、代码、数学。
- 高温：输出更多样、随机、有创意，适合写作、头脑风暴；但可能跑题或幻觉。
- 温度不提升模型知识，只改变选词的随机程度。

**常用建议**：

| 场景 | 建议 |
|---|---|
| 事实 / 代码 / 数学 | 0 ~ 0.3 |
| 通用对话 | 0.6 ~ 1.0 |
| 创意写作 | 0.8 ~ 1.2 |

**注意**：常见范围 0~2，默认常为 1；即使温度为 0，也不保证完全可复现。常与 top_p、top_k 配合使用。

---

## English Version

**What it is**: Temperature controls the randomness of a large language model’s output. Think of it as a “randomness / creativity knob.”

**What it does**:
- Low temperature: more deterministic, stable, conservative. Good for factual QA, code, and math.
- High temperature: more diverse, random, creative. Good for writing and brainstorming, but may drift off-topic or hallucinate.
- Temperature does not increase knowledge; it only changes how randomly tokens are chosen.

**Recommended ranges**:

| Use case | Suggestion |
|---|---|
| Factual / code / math | 0 ~ 0.3 |
| General chat | 0.6 ~ 1.0 |
| Creative writing | 0.8 ~ 1.2 |

**Notes**: Common range is 0~2, default is often 1. Even at temperature 0, output is not guaranteed to be fully reproducible. Often used with top_p and top_k.