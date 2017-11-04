import win32com.client as cli

xl = cli.Dispatch("Excel.Application")
xl.Visible = True
wb = xl.Workbooks.Open('C:\\Users\\machen\\Desktop\\hy_map\\민석.xlsx')
ws = wb.ActiveSheet

with open('minseok.txt', 'w') as f:
    i = 2
    j = 2
    while True:
        A = ws.Cells(i,1).Value

        if A == None:
            break

        try:
            A = int(A)
        except Exception as e:
            pass

        while True:
            path = ws.Cells(i,j).Value

            if path == None:
                print("줄바꿈")
                j = 2
                break

            path = str(path)

            if path == '∞':
                j += 1
            elif path == '0.0':
                j += 1
            else:
                try:
                    B = int(ws.Cells(1,j).Value)
                except Exception as e:
                    B = ws.Cells(1,j).Value
                print(path)
                f.write("(" + str(A) + "," + str(B) + "," + path + "),\n")
                j += 1

        print(str(A), "END")
        i += 1

xl.Quit()
print("THE END")
