# Contribution workflow

1. 新建分支：`paper/<paper-id>`、`module/<name>` 或 `question/<topic>`。
2. 运行 `python scripts/validate_database.py`。
3. PR 描述说明新增证据、可复用模块、受影响问题与未解决风险。
4. 至少一名领域成员检查事实定位，另一名成员检查数据结构与可重复性。

## Definition of done

- 元数据可唯一定位文献
- 至少一个精确证据锚点
- 有局限与反证记录
- 文件间链接有效
- 不含 PDF、患者标识或密钥
