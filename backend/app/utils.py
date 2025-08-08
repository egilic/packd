import uuid

def generate_invite_token(group_id):
    return f"{group_id}-{uuid.uuid4()}"
