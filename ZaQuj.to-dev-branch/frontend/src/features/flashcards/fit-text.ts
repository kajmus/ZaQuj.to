const MAX_FONT_SIZE = 24
const MIN_FONT_SIZE = 12

export function fitTextToContainer(text: HTMLElement, container: HTMLElement) {
  const fits = () =>
    text.scrollWidth <= container.clientWidth &&
    text.scrollHeight <= container.clientHeight

  let smallestFit = MIN_FONT_SIZE
  let largestFit = MAX_FONT_SIZE

  text.style.fontSize = `${MAX_FONT_SIZE}px`
  if (fits()) return

  text.style.fontSize = `${MIN_FONT_SIZE}px`
  if (!fits()) return

  while (largestFit - smallestFit > 0.5) {
    const candidate = (smallestFit + largestFit) / 2
    text.style.fontSize = `${candidate}px`

    if (fits()) {
      smallestFit = candidate
    } else {
      largestFit = candidate
    }
  }

  text.style.fontSize = `${smallestFit}px`
}