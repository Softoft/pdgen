from typing import Iterable, List

from py2puml.domain.umlclass import UmlClass
from py2puml.domain.umlenum import UmlEnum
from py2puml.domain.umlitem import UmlItem
from py2puml.domain.umlrelation import UmlRelation

PUML_FILE_START = """@startuml {diagram_name}
!pragma useIntermediatePackages false

"""
PUML_FILE_FOOTER = """footer Generated by //py2puml//
"""
PUML_FILE_END = """@enduml
"""
PUML_ITEM_START_TPL = """{item_type} {item_fqn} {{
"""
PUML_ATTR_TPL = """  {attr_name}: {attr_type}{staticity}
"""
PUML_ITEM_END = """}
"""
PUML_RELATION_TPL = """{source_fqn} {rel_type}-- {target_fqn}
"""

FEATURE_STATIC = ' {static}'
FEATURE_INSTANCE = ''


def to_puml_content(diagram_name: str, uml_items: List[UmlItem], uml_relations: List[UmlRelation]) -> Iterable[str]:
    yield PUML_FILE_START.format(diagram_name=diagram_name)

    # exports the domain classes and enums
    for uml_item in uml_items:
        if isinstance(uml_item, UmlEnum):
            uml_enum: UmlEnum = uml_item
            yield PUML_ITEM_START_TPL.format(item_type='enum', item_fqn=uml_enum.fqn)
            for member in uml_enum.members:
                yield PUML_ATTR_TPL.format(attr_name=member.name, attr_type=member.value, staticity=FEATURE_STATIC)
            yield PUML_ITEM_END
        elif isinstance(uml_item, UmlClass):
            uml_class: UmlClass = uml_item
            yield PUML_ITEM_START_TPL.format(
                item_type='abstract class' if uml_item.is_abstract else 'class', item_fqn=uml_class.fqn
            )
            for uml_attr in uml_class.attributes:
                yield PUML_ATTR_TPL.format(
                    attr_name=uml_attr.name,
                    attr_type=uml_attr.type,
                    staticity=FEATURE_STATIC if uml_attr.static else FEATURE_INSTANCE,
                )
            yield PUML_ITEM_END
        else:
            raise TypeError(f'cannot process uml_item of type {uml_item.__class__}')

    # exports the domain relationships between classes and enums
    for uml_relation in uml_relations:
        yield PUML_RELATION_TPL.format(
            source_fqn=uml_relation.source_fqn, rel_type=uml_relation.type.value, target_fqn=uml_relation.target_fqn
        )

    yield PUML_FILE_FOOTER
    yield PUML_FILE_END