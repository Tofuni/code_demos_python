def validateEnclosingBrackets(s):
	r = []
	brackets = [
		["(", ")"],
		["{", "}"],
		["[", "]"]
	]
	for c in s:
		for b in brackets:
			if c == b[0]:
				r.append(b[1])
				break
			if c == b[1]:
				if len(r) > 0 and c == r[-1]:
					r = r[:-1]
					break
				else:
					return False
	if len(r) != 0:
		return False
	return True
	
# ------------ tests ------------

tests = [
	"(hello)",
	"((hello worlds))",
	"((hello worlds)))",
	"([{hello worlds}])",
	"(hel[lo w]orl{ds})",
	"(hel[lo {w}]orlds)",
	"(hel[lo w}]orlds)",
	"(hel[lo {w]orlds)",
	"[((hello worlds]))",
	"[[((hello worlds))]",
	"[[((hello worlds))]]",
	"[(hello {wo(rl)ds})]",
	"[(hello {wo(rl}ds})]",
	"[(h[ello {wo](rl)ds})]",
	"[(h[ell]o {wo(rl)ds})]",
	"[(h[ello {wo(rl)ds}])]",
	"[(h[ello {wo(rl)]ds})]",
	"(hello]"
]
for test in tests:
	print(test, "\n", validateEnclosingBrackets(test), "\n\n-------------\n")
input()