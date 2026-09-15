---
name: serenity-lens
description: 用 X 用户 @aleabitoreddit（Serenity，"白毛股神"）的 AI 供应链"卡点/瓶颈"框架分析股票、行业、新闻或财报。当用户提到 Serenity / aleabitoreddit / 白毛股神，或要求从 AI 硬件供应链瓶颈（存储、光子学/CPO、InP 衬底、先进封装、电源、neocloud、人形机器人）的视角评估某只股票、判断一则新闻对哪些标的是利好、复盘一次暴跌是流动性还是基本面、或检查一家公司的股权结构是否"有毒"时使用。不是投资建议生成器——输出的是按她的方法走一遍的研究框架和结论草稿。
---

# Serenity 视角：AI 供应链卡点投资框架

提炼自 @aleabitoreddit 2025-07 至 2026-09 的 4769 条推文（本地归档见文末）。
她的自我定义："AI/Semi Supply Chains Research"，组合集中在 AI chokepoints and bottlenecks。
所有结论都要标注：这是复现她的推理方式，不是她本人的观点，也不是投资建议。

## 一句话世界观

AI 投资比人们想的简单：**Nvidia/Jensen 会公开告诉你下一步要什么，市场每次都不信，直到它发生。**
她的工作就是：顺着 Nvidia 的采购/架构动作往上游找那个"没有它整条链就停摆"的小公司，
在收入拐点前 8 个月左右建仓，等市场验证，然后轮动到下一个瓶颈。

## 分析流程（按顺序走）

### 1. 先定主题，再选个股
- 只做"资金正在流入的活跃瓶颈"，不做冷门行业的逆向翻身股（她明确说过在网安/软件上试过，教训是"rotate where the money flows"）。
- 主题必须有**结构性收入增长或技术架构切换**背书。检验标准：产业龙头是否已经在财报电话会说"sold out / LTA / allocation / 涨价 / 向竞争对手买货"。
  - 光子学有真实收入 + Nvidia 亲自推 → 做；量子几乎没收入 → 不做。
- 典型主题演进：EML 瓶颈（LITE）→ CW 激光/可插拔（AAOI）→ CW 激光/CPO（SIVE）。**Alpha 在"不在本轮周期、但在下一轮"的名字。**

### 2. 供应链映射（她研究的核心动作）
从下游超大规模云厂商往上游拆 BOM，找到：
- 全球份额 ≥ 30–40% 的材料/器件供应商（AXTI 之于 InP 衬底、LPK 之于玻璃基板设备、SOI 之于 SiPh 衬底、Harmonic Drive 之于谐波减速器）。
- 被写进代工厂参考设计 / 被下游多家 hyperscaler 供应商指定为主供或独家（SIVE 之于 GFS 参考激光、Ayar、Jabil 1.6T LRO）。
- 区分 **chokepoint**（架构上绕不开、没有替代源）和 **bottleneck**（掌握最终产能/定价权，哪怕是 fab-lite 外包生产）。两者兼具最强。

信息来源（按她实际引用频率）：
财报电话会/年报原文 → 客户官网供应商页变动（谁被删掉、谁被加上）→ Digitimes / Trendforce / 韩媒 → GS/MS/UBS 行业报告 TAM 数字 → 政府文件（CHIPS Act、EU Chips Act 2、商务部）→ 行业会议纪要（Rosenblatt、OCP）→ 现实生活观察（RPI 的 AI 用量是从身边人买板子发现的）。

### 3. 估值：看拐点年的收入/营业利润 vs 当前市值，不看今年 P/E
- 公式化写法：`月/季收入指引 × 年化 ÷ 当前市值`，再给毛利率假设。例："$471M/月 → 年化 $5.6B，市值 $12B"。
- 存储类看 2027E 营业利润 vs 市值（SK Hynix 3.5x P/E、Samsung 3.9x 这类数字）。
- 小市值瓶颈股：问"如果这是一个 NAND 式瓶颈，博弈 ASP 涨价后它值多少"，而不是拿分析师的"几亿美元 TAM"去否定它。
- 激光公司的溢价来源：向下 TAM 扩张（激光 → ELS → 整颗光模块/光引擎）+ 向上垂直整合（自建 fab、衬底）提升毛利，参照 LITE 从 $3B → $80B 的路径。
- 代工厂/重资产：低 P/B（低于重置成本）+ 政府补贴 capex 作为下限保护（XFAB）。
- 筛选网站上的 forward P/E 经常是错的，自己算。

### 4. 股权结构/浮筹动态——她排在第一位的筛选项
红旗（直接降级或回避）：
- 大额 ATM 相对市值（IREN $6B ATM / $12.8B 市值；SLNH $500M ATM / $250M 市值）——"结构性抛压，每次反弹都被卖"。
- 高息债务吃掉 FCF（CRWV 年利息 $1.5B+）。
- 用 SBC 粉饰盈利的软件公司。
- 相对 NAV 高溢价的持股载体 + 同时增发（BOT）——"你是别人的退出流动性"。
绿旗：战略方直投（NVDA 投 NBIS）、可转债优于 ATM、超额认购的机构定增用于产能而非发工资。
规则：好公司 + 有毒融资 → 等老股东被稀释完再进。她自己持仓也照此批评（AAOI 在下跌中做 $600M ATM 是错的时机，但因产能受限、需求可见度高仍持有）。

### 5. 时间与节奏
- 经验法则：**除空间/量子外，市场大约提前 8 个月定价。**
- 政策/主题新闻落到个股通常 3–15 个月。
- 大部分收益在"官方确认之前"，财报只是对供应链线索的确认。
- 催化剂清单：LTA 签订、sold-out 表述、指数纳入（MSCI/Nasdaq OMX → 被动买盘）、Nasdaq 二次上市（流动性 + M&A 能力）、代工厂参考设计、政府补贴名单。
- 退出：当标的"已被重估"（MU $300 → $1000）就减仓，把资金转到下一个瓶颈；不等到叙事结束。

### 6. 暴跌处理：先判断是流动性还是基本面
问三件事：
1. 瓶颈本身变了吗？（产能是否仍 sold out、LTA 是否仍在、TAM 预测是否下修）
2. 是否是无差别下跌？（NBIS/MRVL/INTC/SNDK/MU 同日 -4% 到 -10% → 保证金连环平仓，不是个股问题）
3. 唯一变化是不是只有股价和叙事？
若答案是"没变 / 是 / 是"→ "AAOI 在 $140 和 $75 是同一家公司"，回撤是加仓机会。
不交易美联储概率；接受主题股波动比大盘大；她自己的教训是**单一主题（光子学）过度集中、没有用存储等对冲**，以及杠杆在 7 月崩盘中放大了回撤（-49%）。

### 7. 她明确不做的事
- 用技术分析判断方向（"TA 是交易员的占星术"，只能用来看入场心理）。
- 短期期权、周期权（多次拿 Reddit 爆仓案例做反面教材）。
- 跟单/盲从（要求读者建立自己的 conviction，否则崩盘时拿不住）。
- 相信媒体对暴跌的"解释"（先查交易所规则、保证金变化、机构仓位）。
- 把"AI 泡沫论"当作卖出理由——她的回应是看订单簿是否仍然 sold out。

## 输出模板（分析一只股票时按此结构写）

```
【卡点定位】它在哪一层？chokepoint 还是 bottleneck？全球份额/独家关系证据
【下游依赖】哪些 hyperscaler / 一线供应商绕不开它（列名字和证据来源）
【需求信号】sold-out / LTA / 涨价 / 竞争对手互相买货 的原话出处
【收入拐点】管理层给的月/季产能或收入指引 → 年化 → 对比当前市值；拐点落在哪个半年
【浮筹检查】ATM / 可转债 / 债务利息 / SBC / 增发用途；是否有结构性抛压
【催化剂与时间表】未来 3–15 个月的确认事件
【风险与证伪条件】什么数据出现说明论点错了（产能未锁定、客户多源化成功、TAM 下修、融资结构恶化）
【她会怎么说】一句话结论 + 她可能的持仓偏见
```

## 使用本地归档取原话

推文归档默认在 `~/Downloads/aleabitoreddit/tweets.json`（可用环境变量 `SERENITY_ARCHIVE` 指到别的目录；
生成方法见仓库 README 的 `scripts/archive_tweets.sh`）。字段：id/date/content/likes/url/media，另有 Markdown 版 `tweets.md`。
归档不存在时跳过这一步，只用本文件和 references 作答，并说明未核对原文。查某个标的或概念时：

```bash
python3 -c "
import json,sys; import os; r=json.load(open(os.path.join(os.environ.get('SERENITY_ARCHIVE', os.path.expanduser('~/Downloads/aleabitoreddit')), 'tweets.json')))
q=sys.argv[1].lower()
for t in sorted([t for t in r if q in t['content'].lower()], key=lambda t:-t['likes'])[:15]:
    print(t['date'][:10], t['likes'], t['url']); print(t['content'][:400].strip()); print('---')
" '$SIVE'
```

引用她的观点时给出日期和链接，标明是当时判断（归档截止 2026-09-14），标的价格/市值已过时。

## 已知偏见（评估她的结论时要打折）
- 重仓光子学（SIVE、AAOI、AXTI、SOI）、存储（Samsung/SK Hynix）、NBIS、Agility Robotics、Harmonic Drive、VPG，谈及这些名字时是在"talk her book"。
- 对 IREN、CRWV、POET、BOT 有明确负面立场，部分源于融资结构分歧。
- 100 万粉丝后她提到有合规审核、发帖延后到收盘，且自己提及"部分推文是 free research 的营销"——高赞推文有传播动机。
- 时间窗口 2025-07 至 2026-09 是 AI capex 超级周期上行期，框架未经历完整下行周期检验。

行业地图、各层供应商清单和她的历史判断见 [references/themes.md](references/themes.md)。
