class Mower:
    def __init__(self, x, y, orientation):
        self.x = x
        self.y = y
        self.orientation = orientation

    def execute_instructions(self, instructions):
    
        for instruction in instructions:
            match instruction:
                case 'D':
                    self.turn_right()
                case 'G':
                    self.turn_left()
                case 'A':
                    self.move_ahead()

                
    def move_ahead(self):
        match self.orientation:
            case 'N':
                self.y += 1
            case 'E':
                self.x += 1
            case 'S':
                self.y -= 1
            case 'W':
                self.x -= 1

    def turn_right(self):
        match self.orientation:
            case 'N':
                self.orientation = 'E'
            case 'E':
                self.orientation = 'S'
            case 'S':
                self.orientation = 'W'
            case 'W':
                self.orientation = 'N'

    def turn_left(self):
        match self.orientation:
            case 'N':
                self.orientation = 'W'
            case 'W':
                self.orientation = 'S'
            case 'S':
                self.orientation = 'E'
            case 'E':
                self.orientation = 'N'
    def correct_position(self, mower,max_x,max_y):
        if mower.x < 0:
            mower.x = 0
        elif mower.x > max_x:
            mower.x = max_x
        if mower.y < 0:
            mower.y = 0
        elif mower.y > max_y:
            mower.y = max_y
            
    def get_position(self):
        return f"{self.x} {self.y} {self.orientation}"


   
if __name__ == "__main__":   
    with open('input.txt', 'r') as f:
        lawn_x, lawn_y = map(int, f.readline().strip().split())
    
        for line in f:
            x, y, orientation = line.split()
            mower = Mower(int(x), int(y), orientation)
        
            instructions = f.readline().strip()
            mower.execute_instructions(instructions)
            mower.correct_position(mower,lawn_x,lawn_y)
            print(mower.get_position())
