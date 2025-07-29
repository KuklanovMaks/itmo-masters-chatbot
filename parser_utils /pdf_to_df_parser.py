import re
from pathlib import Path

import pandas as pd
import pdfplumber


DISCIPLINE_PATTERN = re.compile(r"^([\d,\s]+)\s+(.+?)\s+(\d+)\s+(\d+)$")


def extract_raw_text_from_pdf(pdf_path: Path) -> list[str]:
    """
    Загружает текст со всех страниц PDF и возвращает как список строк.
    """
    extracted = []
    with pdfplumber.open(pdf_path) as doc:
        for page in doc.pages:
            page_text = page.extract_text()
            if page_text:
                extracted.extend(page_text.splitlines())
    return extracted


def parse_line_to_records(line: str) -> list[dict] | None:
    """
    Извлекает данные из строки дисциплины, если она соответствует шаблону.
    """
    match = DISCIPLINE_PATTERN.match(line)
    if not match:
        return None

    sem_raw, title, zet, hours = match.groups()
    semesters = re.findall(r"\d+", sem_raw)

    return [
        {
            "semester": int(sem),
            "discipline": title.strip(),
            "zet": int(zet),
            "hours": int(hours)
        }
        for sem in semesters
    ]


def extract_curriculum_data(pdf_path: Path) -> pd.DataFrame:
    """
    Основная функция: читает PDF и возвращает DataFrame с дисциплинами.
    """
    lines = extract_raw_text_from_pdf(pdf_path)
    records = []

    for line in lines:
        parsed = parse_line_to_records(line)
        if parsed:
            records.extend(parsed)

    return pd.DataFrame(records)


