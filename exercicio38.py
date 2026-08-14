boletim = [[8.0, 7.5, 9.0], [6.5,7.0, 7.5], [9.5, 9.0, 10.0]]
mgeral=0
for i in boletim:
    mgeral=sum(i)+mgeral
    media=sum(i)/3
    print(f"media : {media}")
mgeral=mgeral/9
print(f"media da turma : {mgeral}")   