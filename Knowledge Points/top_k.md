# 大模型参数：Top-K

## 中文版

**是什么**：Top-K 是一种采样限制参数，只从概率最高的 K 个 token 中选下一个词，像“候选词数量旋钮”。

**作用**：
- 小 K：候选少，输出更确定、稳定、保守。
- 大 K：候选多，输出更多样、随机。
- K=1 时相当于每次选最高概率词，接近贪心解码。
- Top-K 不提升模型知识，只限制候选范围。

**常用建议**：

| 场景 | 建议 |
|---|---|
| 事实 / 代码 / 数学 | 1 ~ 20 |
| 通用对话 | 20 ~ 50 |
| 创意写作 | 50 ~ 100 或更大 |

**注意**：常见范围 1~100，默认值因平台而异；固定保留 K 个候选，不随概率分布自适应；常与 temperature、top_p 配合，通常不要同时调到极端。

---

## English Version

**What it is**: Top-K is a sampling limit that chooses the next token only from the K most probable tokens. Think of it as a “candidate count knob.”

**What it does**:
- Small K: fewer candidates; more deterministic, stable, conservative.
- Large K: more candidates; more diverse and random.
- K=1 is close to greedy decoding, always picking the highest-probability token.
- Top-K does not increase knowledge; it only limits the candidate pool.

**Recommended ranges**:

| Use case | Suggestion |
|---|---|
| Factual / code / math | 1 ~ 20 |
| General chat | 20 ~ 50 |
| Creative writing | 50 ~ 100 or larger |

**Notes**: Common range is 1~100; defaults vary by platform. It keeps a fixed number of candidates and does not adapt to the probability distribution. Often used with temperature and top_p; avoid setting all to extremes.