def get_all_collections(vector_db):
    try:
        collections_list = []
        collections = vector_db.get_collections()
        for collection in collections:
            for c in list(collection[1]):
                collections_list.append(c.name)
        return collections_list
    except Exception as e:
        print(f"Error fetching collections from Qdrant: {e}")