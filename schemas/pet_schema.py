PET_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "category": {
            "type": "object",
            "properties": {
                "id": {"type": "number"},
                "name": {"type": "string"}
            }
        },
        "name": {"type": "string"},
        "photoUrls": {"type": "array", "items": {"type": "string"}},
        "tags": {"type": "array"},
        "status": {"type": "string"}
    },
    "required": ["id", "name", "status"]
}