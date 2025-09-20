def is_palindrome(s: str) -> bool:
    """
    引数の文字列が回文であるかを判定します。
    None、空文字、スペースだけの場合は False を返します。

    Parameters
    ----------
    param1 : str
        判定する文字列

    Returns
        回文の場合 True
    ----------
    """
    if not s or not s.strip():
        return False
    return s == s[::-1]
