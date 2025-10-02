export default function Header () {
    return (
        <header className="header" >
            <div className="home_button" onClick={() => window.location.reload()}>
                <img src="../ball.png" alt="logo" className="logo" />
                <h1>Football Infos</h1>
                <img src="../ball.png" alt="logo" className="logo" />
            </div>
        </header>
    )
}