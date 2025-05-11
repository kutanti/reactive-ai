from enum import Enum, auto  # Import Enum

class VectorStoreProvider(Enum):
    QDRANT_CLOUD = auto()  # noqa: QDRANT
    QDRANT_LOCAL = auto()  # noqa: QDRANT