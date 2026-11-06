
import { Link } from 'react-router-dom'
import { useState } from 'react'
import { isSessionActive, startSession } from '../../lib/session'


interface HomeTileProps {
    title: string
    description: React.ReactNode
    accent: string
    icon: React.ReactNode
    to?: string
    disabled?: boolean
    fullWidth?: boolean
    onClick?: () => void
}

function HomeTile({
    title,
    description,
    accent,
    icon,
    to,
    disabled = false,
    fullWidth = false,
    onClick
}: HomeTileProps) {
    const className = `
    flex min-h-40 flex-col items-start justify-between gap-5
    rounded-2xl border-2 bg-white p-6 text-left
    transition-colors
    ${accent}
    ${disabled ? 'cursor-not-allowed opacity-50' : 'hover:bg-slate-50'}
    ${fullWidth ? 'sm:col-span-2' : ''}
  `

    const content = (
        <>
            <div className="flex items-center gap-3">
                <span className="text-current [&_svg]:h-8 [&_svg]:w-8">
                    {icon}
                </span>
                <h2 className="text-xl font-bold">{title}</h2>
            </div>

            <p className="text-sm text-slate-600">
                {description}
            </p>
        </>
    )

    if (disabled) {
        return (
            <button
                type="button"
                disabled
                aria-disabled="true"
                className={className}
            >
                {content}
            </button>
        )
    }

    if (to) {
        return (
            <Link to={to} className={className}>
                {content}
            </Link>
        )
    }

    return (
        <button
            type="button"
            onClick={onClick}
            className={className}
        >
            {content}
        </button>
    )
}

export default function HomePage() {
    const [isLoggedIn, setIsLoggedIn] = useState(isSessionActive)

    function handleLogin() {
        startSession()
        setIsLoggedIn(true)
    }
    return (
        <main className="min-h-screen bg-slate-50 px-5 py-8 text-slate-900 sm:px-8">
            <div className="mx-auto max-w-3xl">
                <header className="mb-10">
                    <p className="text-sm font-semibold uppercase tracking-widest text-indigo-700">
                        ZaQuj.to
                    </p>

                    <h1 className="mt-2 text-3xl font-bold">
                        Co dziś powtarzamy?
                    </h1>

                    <p className="mt-3 text-slate-600">
                        Wybierz sposób nauki i przejdź do działania.
                    </p>
                </header>

                <section
                    aria-label="Dostępne funkcje"
                    className="grid grid-cols-1 gap-4 sm:grid-cols-2"
                >
                    {!isLoggedIn ? (
                        <HomeTile
                            title="Zaloguj się/Załóż konto"
                            description={
                                <>
                                    Zaloguj się, aby uzyskać dostęp do narzędzi nauki.
                                    <br />
                                    <br />
                                    NOTKA: Tymczasowo loguje użytkownika „od razu” - do
                                    zintegrowania z demo logowania, gdy zostanie zaimplementowane.
                                </>
                            }
                            accent="border-indigo-600 text-indigo-700"
                            fullWidth
                            onClick={handleLogin}
                            icon={
                                <svg
                                    viewBox="0 0 24 24"
                                    fill="none"
                                    stroke="currentColor"
                                    strokeWidth="1.8"
                                    strokeLinecap="round"
                                    strokeLinejoin="round"
                                    aria-hidden="true"
                                >
                                    <path d="M15 3h4a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2h-4" />
                                    <path d="M10 17l5-5-5-5" />
                                    <path d="M15 12H3" />
                                </svg>
                            }
                        />
                    ) : (
                        <>
                            <HomeTile
                                title="Fiszki"
                                description="Twórz zestawy i utrwalaj wiedzę za pomocą fiszek."
                                accent="border-teal-700 text-teal-700"
                                to="/flashcards"
                                icon={
                                    <svg
                                        viewBox="0 0 24 24"
                                        fill="none"
                                        stroke="currentColor"
                                        strokeWidth="1.8"
                                        strokeLinecap="round"
                                        strokeLinejoin="round"
                                        aria-hidden="true"
                                    >
                                        <rect x="3" y="4" width="15" height="16" rx="2" />
                                        <path d="M7 8h7M7 12h7M7 16h4" />
                                        <path d="M18 7h3v13a1 1 0 0 1-1 1" />
                                    </svg>
                                }
                            />

                            <HomeTile
                                title="Quizy"
                                description="Sprawdź swoją wiedzę i zobacz, ile już pamiętasz."
                                accent="border-slate-400 text-slate-500"
                                disabled
                                icon={
                                    <svg
                                        viewBox="0 0 24 24"
                                        fill="none"
                                        stroke="currentColor"
                                        strokeWidth="1.8"
                                        strokeLinecap="round"
                                        strokeLinejoin="round"
                                        aria-hidden="true"
                                    >
                                        <circle cx="12" cy="12" r="9" />
                                        <path d="M9.5 9a2.5 2.5 0 1 1 4.2 1.8c-1.1 1-1.7 1.2-1.7 2.7" />
                                        <path d="M12 17h.01" />
                                    </svg>
                                }
                            />
                        </>
                    )}
                </section>
            </div>
        </main>
    )
}
