import abc

from ..model.structureddata import StructuredData


class StructuredDataRepository(abc.ABC):

    @abc.abstractmethod
    def save(self, structured_data: StructuredData) -> None:
        pass
