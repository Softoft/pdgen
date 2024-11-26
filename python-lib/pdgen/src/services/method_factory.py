class MethodFactory:
    def _is_method_excluded(self, method_name: str) -> bool:
        return method_name.startswith(self.EXCLUDE_ATTRIBUTES)

    def _find_all_methods(self) -> list[MethodInformation]:
        return [MethodInformation(func_name, func_ref) for func_name, func_ref
                in inspect.getmembers(self.class_reference, inspect.isfunction)]

    def _find_all_uml_methods(self) -> list[MethodInformation]:
        all_methods = self._find_all_methods()
        for method in all_methods:
            print(method.function_reference.__name__)
            print(hasattr(method.function_reference, '__is_uml_method__'))
        return [method for method in all_methods if hasattr(method.function_reference, '__is_uml_method__')]



    def add_method(self, name: str, return_type: type, parameters: dict[str, type]):
        self.methods.append(UMLMethod(name, return_type, parameters))

    def add_all_methods(self):
        print(f"All Methods: {self._find_all_methods()}")
        uml_methods = self._find_all_uml_methods()
        print(f"UML methods: {uml_methods}")
        for method in uml_methods:
            method_signature: dict[str, type] = typing.get_type_hints(method.function_reference)
            return_type = method_signature.pop('return', type(None))

            # noinspection PyTypeChecker
            self.add_method(name=method.name,
                            return_type=return_type,
                            parameters=method_signature)
