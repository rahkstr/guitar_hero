streak = 0
frame = 0
columns = [
    {
        'key': 'j',
        'x': 220,
        'color': color(255, 0, 100),
        'notes': []
    },{
        'key': 'k',
        'x': 300,
        'color': color(0, 255, 100),
        'notes': []
    },{
        'key': 'l',
        'x': 380,
        'color': color(100, 0, 255),
        'notes': []
    }
]

def setup():
    size(600, 400)

def draw():
    global streak, notes, columns, frame

    if frame % int(frameRate) == 0:
        for column in columns:
            if (len(column['notes']) == 0 or column['notes'][-1] > 30) and int(random(3)) == 0:
                column['notes'].append(-25)
    
    background(0, 0, 0)
    fill(255, 255, 255)
    text(str(streak), 10, 20)
    
    for column in columns:
        # circle
        fill(0, 0, 0)
        stroke(column['color'])
        ellipse(column['x'],300, 70, 70)
        
        # notes
        noStroke()
        fill(column['color'])
        for i in range(len(column['notes'])):
            noteY = column['notes'][i]
            ellipse(column['x'], noteY, 50, 50)
            column['notes'][i] += 1
        if column['notes'][0] >= 425:
            column['notes'].pop(0)

    frame += 1
        
def keyPressed():
    global streak, notes

    for column in columns:
        if key == column['key']:
            for i in range(len(column['notes'])):
                noteY = column['notes'][i]
                if noteY > 280 and noteY < 320:
                    streak += 1
                    column['notes'].pop(i)
                    break
                else:
                    streak = 0
