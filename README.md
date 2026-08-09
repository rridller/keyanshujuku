# Human Skin Regeneration Research OS

面向皮肤类器官、瘢痕再生、烧伤创面感染、耐药铜绿假单胞菌、噬菌体治疗、水凝胶递送及组织工程皮肤的科研知识操作系统。

核心链路：

> Paper → Scientific Question → Experimental Module → Technology Pipeline → Figure Blueprint → Manuscript-ready Text

## 快速开始

1. 将 PDF 放入本地文献管理器（建议 Zotero）；本仓库不提交受版权保护的 PDF。
2. 复制 `01_Literature_Database/paper_notes/PAPER_TEMPLATE.md`，按 `领域缩写-年份-序号` 命名。
3. 在 `01_Literature_Database/papers.yaml` 登记结构化元数据。
4. 将可复用实验步骤沉淀到 `03_Experimental_Modules/`。
5. 将跨实验模块的路线写入 `04_Technology_Pipelines/`。
6. 将图版设计和可引用段落分别沉淀到 `05_Figure_Design/` 与 `06_Manuscript_Building/`。

## 研究主题与 ID

| 前缀 | 主题 |
|---|---|
| `SKIN-ORG` | 皮肤类器官与表皮干细胞 |
| `SCAR-ORG` | 增生性瘢痕与瘢痕疙瘩 |
| `BURN-INFECT` | 烧伤创面感染 |
| `MDR-PA` | 耐药铜绿假单胞菌与生物膜 |
| `PHAGE` | 个体化裂解性噬菌体治疗 |
| `HYDROGEL` | 水凝胶与局部递送 |
| `REGEN` | 血管化、ECM 支架与组织工程皮肤 |

## 数据原则

- 区分原文事实、作者解释和本课题组推断。
- 所有结论必须带来源定位（DOI/PMID、图表或页码）。
- `manuscript_ready` 是重新表述的草稿，禁止复制原文长句。
- 患者、菌株及未公开实验数据必须脱敏；仓库默认设为 Private。
- 二进制数据和大文件使用 Git LFS 或外部存储，只在仓库保存索引与校验值。

## 目录

- `01_Literature_Database`：文献主表、BibTeX 与单篇拆解笔记
- `02_Scientific_Questions`：按研究方向维护问题树
- `03_Experimental_Modules`：可复用实验单元
- `04_Technology_Pipelines`：端到端技术路线
- `05_Figure_Design`：图版蓝图与图形摘要
- `06_Manuscript_Building`：按章节维护可引用论证单元
- `07_Protocols`：版本化 SOP（不含敏感信息）
- `08_AI_Knowledge_Base`：提示词、RAG 元数据与检索规范
- `09_Templates`：统一模板
- `scripts`：本地校验和 Zotero CSV 导入工具

## GitHub 建议

建立私有仓库后，保护 `main` 分支，通过 PR 合并；开启 Issues、Projects 与 Dependabot。标签建议：`topic:*`、`stage:*`、`evidence:*`、`priority:*`。
