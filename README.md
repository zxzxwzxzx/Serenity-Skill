# Serenity-Skill

一个 [Claude Code](https://claude.com/claude-code) skill：让 Claude 按 X 用户 **@aleabitoreddit（Serenity，"白毛股神"）** 的
"AI 供应链卡点 / 瓶颈"框架来分析股票、行业、新闻和财报。

方法论提炼自她 2025-07 至 2026-09 期间的 4769 条公开推文（1524 条原创 + 3245 条回复），
重点读了其中 863 条 400 字以上的长文。仓库只包含**提炼后的框架**，不包含推文原文。

> 这不是投资建议，也不代表 Serenity 本人。它把她公开表达过的推理方式整理成可复用的分析步骤，
> 输出的是"按她的方法走一遍"的研究草稿，最终判断和风险由使用者自己承担。

---

## 目录

```
Serenity-Skill/
├── SKILL.md                  # skill 主体：方法论 + 分析流程 + 输出模板 + 已知偏见
├── references/
│   └── themes.md             # 主题演进表、CPO 供应链 13 层地图、"瓶颈成立"证据 checklist、历史 call
└── scripts/
    ├── archive_tweets.sh     # （可选）用 gallery-dl 归档任意 X 用户的全部推文
    └── merge.py              # 把归档合并成 tweets.json / tweets.md
```

---

## 安装

**方式 A：全局安装（所有项目可用）**

```bash
git clone https://github.com/zxzxwzxzx/Serenity-Skill.git
mkdir -p ~/.claude/skills
cp -r Serenity-Skill ~/.claude/skills/serenity-lens
```

**方式 B：只装到某个项目**

```bash
cp -r Serenity-Skill <your-project>/.claude/skills/serenity-lens
```

目录名可以随意，Claude Code 以 `SKILL.md` 里 frontmatter 的 `name: serenity-lens` 识别。
安装后重新打开 Claude Code，`/serenity-lens` 应出现在可用 skill 列表中。

---

## 使用

skill 会在下面这些场景自动触发，也可以手动 `/serenity-lens` 调用：

| 你问的 | 它做的 |
|---|---|
| "用 Serenity 的视角看 $XXX" | 按 8 段输出模板走一遍：卡点定位 → 下游依赖 → 需求信号 → 收入拐点 vs 市值 → 浮筹检查 → 催化剂 → 证伪条件 → 一句话结论 |
| "这条新闻（比如 AMD 抢 CW 激光 LTA）对谁是利好" | 把新闻映射到 references 里的供应链分层，找到上游受益者 |
| "今天 AI 股集体暴跌，是基本面还是流动性" | 走她的"暴跌三问"：瓶颈变了吗 / 是无差别下跌吗 / 是否只有股价变了 |
| "这家公司的融资结构有没有问题" | 按她排第一位的筛选项检查 ATM / 可转债 / 债务利息 / SBC / NAV 溢价 |
| "她对 $SIVE 怎么看" | 若本地有推文归档，回查原文并给出日期和链接；没有则基于 references 作答并注明未核对原文 |

示例：

```
> 用 serenity 的框架分析一下 Soitec
> 按白毛股神的思路，Micron 签 QCOM 的 LTA 之后为什么反而跌了
> /serenity-lens 检查 IREN 的股权结构
```

---

## 框架速览（详见 SKILL.md）

她的一句话世界观：**Nvidia/Jensen 会公开告诉你下一步要什么，市场每次都不信，直到它发生。**
所以工作就是顺着 Nvidia 的采购 / 架构动作往上游找"没有它整条链就停摆"的小公司，
在收入拐点前 ~8 个月建仓，等市场验证，然后轮动到下一个瓶颈。

分析顺序：

1. **先定主题，再选个股** —— 只做资金正在流入的活跃瓶颈；主题必须有结构性收入或架构切换背书（光子学有真实收入 → 做；量子没收入 → 不做）。
2. **供应链映射** —— 从 hyperscaler 往上拆 BOM，找份额 ≥30–40% 或被写进代工厂参考设计的供应商；区分 chokepoint（绕不开）和 bottleneck（掌握最终产能/定价）。
3. **估值** —— 看拐点年收入/营业利润 vs 当前市值，不看今年 P/E；激光公司的溢价来自 TAM 向下扩张 + 向上垂直整合。
4. **股权结构** —— 她排第一位的筛选项：大额 ATM、高息债务、SBC 粉饰、NAV 溢价载体都是红旗；好公司 + 有毒融资 → 等老股东被稀释完再进。
5. **时间节奏** —— 市场提前约 8 个月定价（空间/量子除外）；大部分收益在官方确认之前；已被重估就减仓轮动。
6. **暴跌处理** —— 先判断是杠杆连环平仓还是瓶颈本身变了；"AAOI 在 $140 和 $75 是同一家公司"。
7. **她不做的事** —— TA 判方向、短期期权、跟单、相信媒体对暴跌的解释。

---

## （可选）生成推文归档，让 skill 能引用原文

skill 在本地存在 `tweets.json` 时会回查原话并给出日期和链接。归档需要你自己生成：

```bash
pip install gallery-dl        # 需要 Chrome 里已登录 X
scripts/archive_tweets.sh aleabitoreddit            # 默认输出到 ~/Downloads/aleabitoreddit/
# 或指定目录并告诉 skill：
scripts/archive_tweets.sh aleabitoreddit /path/to/dir
export SERENITY_ARCHIVE=/path/to/dir
```

脚本分两遍跑：第一遍下载带媒体的推文及其元数据；第二遍用 `--no-download` + `event=post` 的
metadata 后处理器把**纯文字推文**也写成 JSON（gallery-dl 的 `--write-metadata` 对没有文件的推文不生效，
这是最容易漏掉的一点）。最后 `merge.py` 合并成按时间排序的 `tweets.json` 和可阅读的 `tweets.md`。

注意事项：

- X 会按 15 分钟窗口限流，gallery-dl 会自动等待；7000 条左右的账号完整跑完约 1.5–2 小时。
- macOS 第一次运行会弹 Keychain 授权框（读取 Chrome Safe Storage），选"始终允许"。
- 若日志出现 `cookies: database disk image is malformed`，是 Chrome 正在写 cookie 库导致拷贝损坏，脚本会自动重试。
- 默认排除转推（`retweets=false`），只保留该用户自己写的内容；需要转推可自行改脚本。
- 归档内容属于原作者，仅供个人研究，不要再分发。`.gitignore` 已排除这些文件。

---

## 已知局限与偏见

SKILL.md 末尾有一节专门列出，评估她的结论时请打折：

- 她重仓光子学（SIVE、AAOI、AXTI、SOI）、存储（Samsung / SK Hynix）、NBIS、Agility Robotics 等，谈这些名字时是在 talk her book。
- 对 IREN、CRWV、POET、BOT 有明确负面立场，部分源于融资结构分歧。
- 100 万粉丝后她提到发帖需要合规审核并延后到收盘，高赞推文有传播动机。
- 样本窗口 2025-07 至 2026-09 是 AI capex 超级周期上行期，框架没有经历完整下行周期的检验。
- 她自述的"25 个 100–1000%+ 的 call"存在幸存者偏差，未系统披露失败案例。
- 归档截止 2026-09-14，references 里的价格、市值、持仓都是当时快照。

---

## 更新框架

推文归档更新后，重新读长文并修订 `SKILL.md` / `references/themes.md` 即可；
两个文件都是纯 Markdown，没有构建步骤。欢迎 PR 补充她后续的新主题或修正理解偏差。

## License

MIT（仅指本仓库的框架文本和脚本；推文原文版权归 @aleabitoreddit 所有）。
