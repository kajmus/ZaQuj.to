
import { Link } from 'react-router-dom'
import { useState } from 'react'
import { isSessionActive } from '../../lib/session'
import CategorySelector from '../categories/CategorySelector'


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
    const [isLoggedIn] = useState(isSessionActive)

    return (
        <main className="min-h-screen bg-slate-50 px-5 py-8 text-slate-900 sm:px-8">
            <div className="mx-auto max-w-3xl">
                <header className="mb-10">
                    <div className="flex items-start justify-between gap-4">
                        <div>
                            <p className="text-sm font-semibold uppercase tracking-widest text-indigo-700">
                                ZaQuj.to
                            </p>

                            <h1 className="mt-2 text-3xl font-bold">
                                Co dziś powtarzamy?
                            </h1>

                            <p className="mt-3 text-slate-600">
                                Wybierz sposób nauki i przejdź do działania.
                            </p>
                        </div>

                        {isLoggedIn && (
                            <button
                                type="button"
                                disabled
                                aria-disabled="true"
                                className="shrink-0 cursor-not-allowed rounded-lg border border-slate-300 bg-white px-4 py-2 text-sm font-semibold text-slate-500 opacity-60"
                            >
                                Mój profil
                            </button>
                        )}
                    </div>
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
                                    Zaloguj się lub załóż konto, aby uzyskać dostęp do narzędzi nauki.
                                </>
                            }
                            accent="border-indigo-600 text-indigo-700"
                            fullWidth
                            to="/login"
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
                                title="Wszystkie"
                                description="Wybierz tryb nauki dla pytań z całej bazy."
                                accent="border-indigo-700 text-indigo-700"
                                to="/all"
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
                                        <path d="M4 5h16M4 12h16M4 19h16" />
                                        <circle cx="7" cy="5" r="1" fill="currentColor" />
                                        <circle cx="12" cy="12" r="1" fill="currentColor" />
                                        <circle cx="17" cy="19" r="1" fill="currentColor" />
                                    </svg>
                                }
                            />

                            <HomeTile
                                title="Powtórka"
                                description="Wróć do pytań, które wymagają jeszcze utrwalenia."
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
                                        <path d="M3 12a9 9 0 0 1 15.4-6.4L21 8" />
                                        <path d="M21 3v5h-5M21 12a9 9 0 0 1-15.4 6.4L3 16" />
                                        <path d="M3 21v-5h5" />
                                    </svg>
                                }
                            />
                        </>
                    )}
                </section>

                {isLoggedIn && (
                    <section aria-labelledby="categories-heading" className="mt-10">
                        <h2 id="categories-heading" className="mb-4 text-xl font-bold">
                            Kategorie
                        </h2>
                        <CategorySelector />
                    </section>
                )}
            </div>
        </main>
    )
}
