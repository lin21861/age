driving = input('請問你有開過車嗎？')
if driving != '有' and driving != '沒有':
	print('只能輸入：有/沒有')
	raise SystemExit #觸發錯誤，系統離開

age = input('請問你的年齡?')
age = int(age)
if driving == '有':
	if age >= 18:
		print('你通過測驗了')
	else:
		print('奇怪，你怎麼會開過車')
elif driving == '沒有':
	if age >= 18:
		print('你可以去考試了')
	else:
		print('那你要繼續等待了')

		
#else:
	#print('只能輸入：有/沒有')
