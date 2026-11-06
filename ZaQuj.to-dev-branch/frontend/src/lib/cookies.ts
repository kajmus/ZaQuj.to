// Prosty helper na obsługę ciasteczek

export function getCookie(name: string): string | undefined {
  const prefix = `${encodeURIComponent(name)}=`

  const cookie = document.cookie
    .split('; ')
    .find((item) => item.startsWith(prefix))

  if (!cookie) {
    return undefined
  }

  return decodeURIComponent(cookie.slice(prefix.length))
}

export function setCookie(name: string, value: string): void {
  document.cookie = [
    `${encodeURIComponent(name)}=${encodeURIComponent(value)}`,
    'Path=/',
    'Max-Age=86400',
    'SameSite=Lax',
  ].join('; ')
}

export function deleteCookie(name: string): void {
  document.cookie = [
    `${encodeURIComponent(name)}=`,
    'Path=/',
    'Max-Age=0',
    'SameSite=Lax',
  ].join('; ')
}
