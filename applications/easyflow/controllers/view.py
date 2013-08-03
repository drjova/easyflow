def index():
    """
    """
    occurrences = db(db.occurrence.user_id == auth.user_id).select()
    return dict(occurrences = occurrences[0]["status_id"], app = "")
