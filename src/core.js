// function "equal" has type (a -> (a -> Atom))
function equal(a, b) {
  return a === b || Array.isArray(a) ? JSON.stringify(a) === JSON.stringify(b) : false
}
