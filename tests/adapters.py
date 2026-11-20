from __future__ import annotations

import os
from typing import Any
from resiliparse.parse.html import HTMLTree
from resiliparse.extract import html2text
from concurrent.futures import ThreadPoolExecutor
import re


def run_extract_text_from_html_bytes(html_bytes: bytes) -> str | None:
    html_tree = HTMLTree.parse_from_bytes(html_bytes, encoding="utf-8")
    return html2text.extract_plain_text(html_tree)


def run_identify_language(text: str) -> tuple[Any, float]:
    """
    You can download the fastText language
identification model lid.176.bin from https://fasttext.cc/docs/en/language-identification.html; it is also
available at /shared-data/classifiers/lid.176.bin.
English (“en”) and Chinese (“zh”)
    """
    import torch

    model = torch.load("lid.176.bin", map_location=torch.device("cpu"))
    model.eval()
    result = model(text)
    raise result

def run_mask_emails(text: str) -> tuple[str, int]:
    import re
    MASK = '|||EMAIL_ADDRESS|||'
    pattern = r"\b\w+@\w+\.\w+"
    match = re.findall(pattern, text)
    for email in match:
        text = text.replace(email, MASK)
    return (text, len(match))


def run_mask_phone_numbers(text: str) -> tuple[str, int]:
    import re
    MASK = '|||PHONE_NUMBER|||'
    pattern = r'-'



def run_mask_ips(text: str) -> tuple[str, int]:
    pattern = r''
    fixed_size = 12
    for i in range(0, len(text)):
        if text[i] >= '0' or text[i] <= '9':
            substr = text[i : fixed_size]

def is_valid_ipv4(text: str) -> bool:
    pattern = r"^(25[0-5])"


def run_classify_nsfw(text: str) -> tuple[Any, float]:
    """
    dolma-artifacts.org/.../jigsaw_fasttext_bigrams_nsfw_final.bin.
    """
    raise NotImplementedError


def run_classify_toxic_speech(text: str) -> tuple[Any, float]:
    raise NotImplementedError


def run_classify_quality(text: str) -> tuple[Any, float]:
    raise NotImplementedError


def run_gopher_quality_filter(text: str) -> bool:
    raise NotImplementedError

executor = ThreadPoolExecutor(max_workers=2)

def run_exact_line_deduplication(
    input_files: list[os.PathLike], output_directory: os.PathLike
):
    def getfiles() -> list:
        files = []
        from pathlib import Path
        for file_path in input_files:
            path = Path(file_path)
            if path.exists() and path.is_file():
                files.append(tuple(path.name, path))
        return files

    def deduplicate(file) -> None:
        (name, path) = file
        with open(path, 'r', encoding='utf-8'):
            text = path.read()

        text = re.sub(r'\n+', ' ', text)
        sentences = re.split(r'(?<=[.!?])\s+', text)

        stripped_sentences = [s.strip() for s in sentences if s.strip()]
        visited = set()

        result = []
        for i in range(0, len(stripped_sentences)):
            key = hash(stripped_sentences[i])
            if key not in visited:
                result.append(stripped_sentences[i])

        concat_file_path = output_directory + name
        with open(concat_file_path, 'w', encoding='utf-8'):
            for line in result:
                concat_file_path.write(line + '\n')

    input_file_obj = getfiles()

    for file in input_file_obj:
        deduplicate(file)


def run_minhash_deduplication(
    input_files: list[os.PathLike],
    num_hashes: int,
    num_bands: int,
    ngrams: int,
    jaccard_threshold: float,
    output_directory: os.PathLike,
):
    raise NotImplementedError
