from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
required = [
    "README.md",
    "01_Literature_Database/papers.yaml",
    "01_Literature_Database/references.bib",
    "01_Literature_Database/paper_notes/PAPER_TEMPLATE.md",
    "05_Figure_Design/FIGURE_TEMPLATE.md",
    "07_Protocols/PROTOCOL_TEMPLATE.md",
]

missing = [item for item in required if not (ROOT / item).exists()]
pdfs = list(ROOT.rglob("*.pdf"))
text = (ROOT / "01_Literature_Database/papers.yaml").read_text(encoding="utf-8")
required_keys = ["schema_version:", "papers:", "scientific_question:", "experimental_modules:", "figures:", "manuscript_ready:", "provenance:"]
missing_keys = [key for key in required_keys if key not in text]

if missing or pdfs or missing_keys:
    if missing:
        print("Missing required files:", *missing, sep="\n- ")
    if pdfs:
        print("PDF files must not be committed:", *pdfs, sep="\n- ")
    if missing_keys:
        print("papers.yaml missing keys:", *missing_keys, sep="\n- ")
    sys.exit(1)

print("Research OS structure validation passed.")
