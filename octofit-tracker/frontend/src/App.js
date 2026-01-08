

import logo from './logo.svg';


function App() {
  return (
    <Router>
      <nav className="navbar navbar-expand-lg navbar-dark bg-primary shadow">
        <div className="container-fluid">
          <Link className="navbar-brand d-flex align-items-center fw-bold" to="/">
            <img src={logo} alt="Octofit Logo" className="App-logo" />
            Octofit Tracker
          </Link>
          <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav ms-auto">
              <li className="nav-item">
                <Link className="nav-link" to="/activities">Attività</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/leaderboard">Classifica</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/teams">Squadre</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/users">Utenti</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/workouts">Allenamenti</Link>
              </li>
            </ul>
          </div>
        </div>
      </nav>
      <div className="container py-4">
        <div className="row justify-content-center">
          <div className="col-12 col-lg-10">
            <Routes>
              <Route path="/activities" element={<Activities />} />
              <Route path="/leaderboard" element={<Leaderboard />} />
              <Route path="/teams" element={<Teams />} />
              <Route path="/users" element={<Users />} />
              <Route path="/workouts" element={<Workouts />} />
              <Route path="/" element={
                <div className="text-center mt-5">
                  <h1 className="display-4 fw-bold mb-3">Benvenuto in Octofit Tracker!</h1>
                  <p className="lead">Gestisci attività, squadre, allenamenti e molto altro con stile.</p>
                  <Link to="/activities" className="btn btn-primary btn-lg mt-3">Vai alle Attività</Link>
                </div>
              } />
            </Routes>
          </div>
        </div>
      </div>
    </Router>
  );
}

export default App;
