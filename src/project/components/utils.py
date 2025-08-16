def position_window(screen_wid: int, size: int) -> int:
    """
    Calcula a posição para que a window fique exatamente no meio da tela.
    """
    return int((screen_wid // 2) - (size // 2))