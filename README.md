# Wzorce projektowe

## Materiały
* "Wzorce projektowe. Elementy oprogramowania" E. Gamma, R. Helm, R. Johnson, J. Vlissides
* https://refactoring.guru/pl/design-patterns

## Zadania
1. Poprawne rozwiązanie powinno przechodzić wszystkie testy uruchomione za pomocną `python -m unittest`
2. Wzorzec projektowy Budowniczy
    * zaimplementuj klasę `Window` reprezentującą okno programu graficznego
    * umieść klasę w pliku `window.py`
    * klasa ma przyjmować jako argumenty swojego konstruktora:
        * `x` - składową x położenia okna (domyślna wartość 0)
        * `y` - składową y położenia okna (domyślna wartość 0)
        * `width` - szerokość okna (domyślna wartość 100)
        * `height` - wysokość okna (domyślna wartość 100)
        * `title` - tytuł okna (domyślna wartość `""`)
    * klasa `Window` ma mieć metody zwracające poszczególne atrybuty (getter) o nazwie `get_<atrybut>` gdzie `atrybut` to konkretny atrybut,
    * stwórz klasę `Builder` w pliku `window.py`  pełniącą rolę Budowniczego klasy `Window`.
    * Budowniczy ma być zwracany za pomocą metody `new_builder()` klasy `Window`, metoda ma być oznaczona jako `@staticmethod`
    * klasa `Builder` ma mieć betodę `build()` zwracającą zbudowany obiekt `Window`
    * klasa `Builder` ma mieć metody inicjalizujące poszczególne elementy okna, ich nazwy powinny być takie same jak nazwy parametrów okna
    * przykład użycia wspomnianych meteod \

      ```python
      builder = Window.new_builder()
      window = builder
                 .x(20)
                 .y(30)
                 .height(200)
                 .width(300)
                 .title("New window")
                 .build();
      ```

      lub

      ```python
      window = Window.new_builder()
                 .x(20)
                 .y(30)
                 .height(200)
                 .width(300)
                 .title("New window")
                 .build();
      ```
      
3. Wzorzec projektowy Iterator
   * stwórz klasę `MyTriple` reprezentującą trójkę elementów
   * umieść tę klasę w pliku `triple.py`
   * klasa powinna posiadać konstruktor pozwalający na jej poprawną inicjalizację