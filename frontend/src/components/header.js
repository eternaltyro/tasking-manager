import React from 'react';
import { connect } from "react-redux";
import { Link } from "react-router-dom";
import Popup from "reactjs-popup";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faExternalLinkAlt } from '@fortawesome/free-solid-svg-icons';

import { ORG_URL, ORG_NAME, API_URL } from '../config';
import logo from '../assets/img/main-logo.svg';
import { Dropdown } from './dropdown';
import { Button } from './button';
import { BurgerMenu } from './burgerMenu';



class Header extends React.Component {
  renderMenuItens() {
    const linkCombo = "link ph3 barlow-condensed blue-dark f4 ttu";
    return(
      <div className="v-mid">
        <Link to={'/projects'} className={ linkCombo }>Explore projects</Link>
        <Link to={'/learn'} className={ linkCombo }>How it works</Link>
        <Link to={'/about'} className={ linkCombo }>About</Link>
        <Link to={'/help'} className={ linkCombo }>Help</Link>
      </div>
    );
  }
  render() {
    return (
      <header className="w-100">
        <div className="cf ph2 bb b--grey-light red pt3 pb2">
          <div className="fl w-50">
            <span className="barlow-condensed f5 ml2 ">Mapping our world together</span>
          </div>
          <div className="tr">
            <a className="link red f6 mr2" href={`http://${ORG_URL}`}>
              {ORG_URL} <FontAwesomeIcon icon={faExternalLinkAlt} />
            </a>
          </div>
        </div>
        <div className="mt3 mb2 mh2 header-grid">
          <div className="cf fl grid-area-a">
            <Link to={'/'} className="link mv-1">
              <img src={logo} alt={`${ORG_NAME} logo`} className="ml2 v-mid pb2"
                style={{width: '54px'}}
                />
              <span className="barlow-condensed f3 fw6 ml2 blue-dark">
                Tasking Manager
              </span>
            </Link>
          </div>

          <nav className="grid-area-b mv1">
            { this.renderMenuItens() }
          </nav>

          <div className="fr grid-area-c tr">
            <Dropdown
              onAdd={() => {}}
              onRemove={() => {}}
              onChange={() => {}}
              value={this.props.userPreferences.language || 'English'}
              options={[{label: 'English'}, {label: 'Portuguese (pt)'}]}
              display={this.props.userPreferences.language || 'Language'}
              className="blue-dark bg-white mr1 dn dib-l"
            />
          <a href={`${API_URL}auth/login?redirect_to=/login/`} className="mh1 dn dib-ns">
              <Button className="blue-dark bg-white">Log in</Button>
            </a>
            <Button className="bg-blue-dark white ml1 dn dib-ns">Sign in</Button>
            <div className="dib dn-l">
              <Popup
                trigger={<BurgerMenu />}
                modal
                closeOnDocumentClick
                >
                <div>{ this.renderMenuItens() }</div>
              </Popup>
            </div>
          </div>
        </div>
      </header>
    );
  }
}

const mapStateToProps = state => ({
  userPreferences: state.preferences
});

Header = connect(mapStateToProps)(Header);

export { Header };
