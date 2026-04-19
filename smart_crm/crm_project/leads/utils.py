def calculate_score(status, source):
    score = 0

    status = status.lower()
    source = source.lower()
    
    if status == "converted":
        return 100
    elif status == "lost":
        return 0
    elif status == "interested":
        score += 50
    elif status == "contacted":
        score += 30
    elif status == "new":
        score += 10

    if source == "instagram":
        score += 20
    elif source == "website":
        score += 15
    elif source == "ads":
        score += 10

    return score