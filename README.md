# keyanshujuku · 科研知识数据库

面向皮肤类器官、瘢痕再生、烧伤创面感染、耐药铜绿假单胞菌、噬菌体治疗与水凝胶递送的科研知识操作系统。

核心链路：

> Literature → Scientific Question → Experimental Module → Figure Design → Manuscript

## 数据库结构

```text
keyanshujuku/
├── README.md
├── Literature/
│   ├── papers.yaml
│   ├── references.bib
│   └── notes/
├── Scientific_Questions/
│   ├── skin_organoid.md
│   ├── scar_regeneration.md
│   ├── phage_therapy.md
│   └── wound_infection.md
├── Experimental_Modules/
│   ├── organoid_culture.md
│   ├── scRNAseq.md
│   ├── hydrogel_delivery.md
│   └── infection_model.md
├── Figure_Design/
│   ├── Figure1_model.md
│   ├── Figure2_mechanism.md
│   └── Figure3_validation.md
├── Manuscript/
│   ├── Introduction.md
│   ├── Results.md
│   └── Discussion.md
└── Protocols/
    └── README.md
```

## 使用方法

1. 每篇新文献复制 `Literature/notes/PAPER_TEMPLATE.md`，使用 `主题-年份-序号` 作为 `paper_id`。
2. 在 `Literature/papers.yaml` 登记元数据、科学问题、实验模块、图版与写作用途。
3. 把可复用的方法沉淀到 `Experimental_Modules`，不要只留在单篇文献笔记中。
4. 用 `Figure_Design` 组织论文的证据链，用 `Manuscript` 组织可追溯的论证段落。
5. SOP 和版本记录统一保存在 `Protocols`。

## 数据规范

- 区分原文事实、作者解释和本课题组推断。
- 关键结论必须定位到 DOI/PMID 以及 Figure、Table 或页码。
- 不提交受版权保护的 PDF、患者身份信息、密钥或未脱敏原始数据。
- `Manuscript` 内容应为原创改写，并回链至文献 ID。
