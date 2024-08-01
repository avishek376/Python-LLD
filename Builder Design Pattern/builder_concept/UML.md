![img.png](img.png)

    **Product**: 
                The Product being built.
    **IBuilder[Builder Interface]** 
                Interface: The Interface that the Concrete builder should implement.
    **Concrete Builder[Builder Implementation]**: 
                Provides methods to build and retrieve the concrete product. Implements the Builder Interface.
    **Director**:
                Has a construct() method that when called creates a customized product using the methods of the Builder.