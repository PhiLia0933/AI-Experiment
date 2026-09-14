# 大模型参数：Top-P

## 中文版

**是什么**：Top-P 又叫核采样，按概率从高到低累加，只保留累计概率达到 P 的那部分 token，像“动态候选范围旋钮”。

**作用**：
- 小 P：候选少，输出更确定、稳定、保守。
- 大 P：候选多，输出更多样、随机、有创意。
- P=1 时保留全部候选；P 接近 0 时接近只选最高概率词。
- Top-P 不提升模型知识，只限制候选范围。

**常用建议**：

| 场景 | 建议 |
|---|---|
| 事实 / 代码 / 数学 | 0.1 ~ 0.5 |
| 通用对话 | 0.7 ~ 0.95 |
| 创意写作 | 0.9 ~ 1.0 |

**注意**：常见范围 0~1，默认常为 1；候选数量会随概率分布自动变化；常与 temperature、top_k 配合，通常优先调 temperature 或 top_p，避免同时极端。

---

## English Version

**What it is**: Top-P, also called nucleus sampling, keeps the smallest set of tokens whose cumulative probability reaches P. Think of it as a “dynamic candidate range knob.”

**What it does**:
- Small P: fewer candidates; more deterministic, stable, conservative.
- Large P: more candidates; more diverse, random, creative.
- P=1 keeps all candidates; P near 0 is close to picking only the highest-probability token.
- Top-P does not increase knowledge; it only limits the candidate pool.

**Recommended ranges**:

| Use case | Suggestion |
|---|---|
| Factual / code / math | 0.1 ~ 0.5 |
| General chat | 0.7 ~ 0.95 |
| Creative writing | 0.9 ~ 1.0 |

**Notes**: Common range is 0~1, default is often 1. The number of candidates adapts to the probability distribution. Often used with temperature and top_k; usually tune temperature or top_p first, and avoid setting all to extremes.