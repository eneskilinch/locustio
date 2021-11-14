from base.base_functions import Base


class PageBase(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
