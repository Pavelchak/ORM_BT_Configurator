from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref

from ..base import Base, IGeneral


class Component(Base, IGeneral):
    __tablename__ = 'component'
    id = Column(Integer, primary_key=True)
    element_id = Column(String(8), nullable=False)
    component_class = Column(String(30), nullable=False)
    container = Column(String, nullable=False)
    text = Column(String(50))
    name = Column(String(50))
    title = Column(String(50))
    component_id = Column(Integer, ForeignKey('component.id'))
    # child_components = relationship("Component")
    child_components = relationship("Component", backref=backref('parent_component', remote_side=[id]))

    def __init__(self, element_id, component_class, container, text, name, title, component_id):
        # type: (str, str, str, str, str, str, int) -> None
        self.element_id = element_id
        self.component_class = component_class
        self.container = container
        self.text = text
        self.name = name
        self.title = title
        self.component_id = component_id

    def __repr__(self):
        return "Profile(%s, '%s', '%s', '%s', '%s', '%s', %s, %s)" % (
            self.id, self.element_id, self.component_class, self.text, self.name, self.title, self.container,
            self.component_id)

    def full_update(self, obj):
        self.element_id = obj.element_id
        self.component_class = obj.component_class
        self.container = obj.container
        self.text = obj.text
        self.name = obj.name
        self.title = obj.title
        self.component_id = obj.component_id
