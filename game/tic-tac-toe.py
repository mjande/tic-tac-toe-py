class Board:
    """Represents a 3x3 tic-tac-toe board"""
    def __init__(self) -> None:
        self.matrix = [[None for _ in range(3)] for _ in range(3)]
        
    def render(self) -> None:
        print('    0   1   2')

        
        for row in range(len(self.matrix)):
            print(row, end=' | ')
            
            
            for col in range(len(self.matrix[0])):
                square = self.matrix[row][col]
                if square is None:
                    print('N', end=' | ')
                else:
                    print(square, end=' ')
            
            print()
            print('   -----------')


Board().render()
