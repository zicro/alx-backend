#!/usr/bin/env python3
"""
Simple pagination
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return the start and end index for a given page and page size.
    """
    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size

    return (start_idx, end_idx)
