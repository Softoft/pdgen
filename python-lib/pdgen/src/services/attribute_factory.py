class UMLAttributeFactory:
    def add_attribute(self, type_info: TypeInformation):
        self.attributes.append(UMLAttribute(type_info.name, type_info.type))

    def add_all_attributes(self):
        class_attrs: list[TypeInformation] = get_type_hint_information(self.class_reference)
        init_attrs: list[TypeInformation] = get_type_hint_information(self.class_reference.__init__)
        print(init_attrs)
        print(class_attrs)
        union_attrs: list[TypeInformation] = list(set(class_attrs) | set(init_attrs))
        print(f"union:  {union_attrs}")
        filtered_attrs: list[TypeInformation] = list(filter(
            lambda x: not self._is_attribute_excluded(x), union_attrs))
        print(filtered_attrs)
        for type_info in filtered_attrs:
            self.add_attribute(type_info)


    def _is_attribute_excluded(EXCLUDE_ATTRIBUTES, type_info: TypeInformation) -> bool:
        return type_info.name.startswith(EXCLUDE_ATTRIBUTES)