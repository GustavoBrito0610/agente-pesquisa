def atualizar_humor(memoria, msg):

    msg = msg.lower()

    if any(x in msg for x in [
        "triste",
        "mal",
        "sozinho",
        "cansado"
    ]):

        memoria["humor"] = "protetora"

    elif any(x in msg for x in [
        "feliz",
        "animado"
    ]):

        memoria["humor"] = "feliz"

    else:

        memoria["humor"] = "neutro"