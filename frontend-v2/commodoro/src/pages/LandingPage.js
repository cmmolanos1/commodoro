import React,{Fragment} from 'react';
import Header from "../components/Header";
import PageHeader from "../components/PageHeader";
import LandingPage from "../components/LandingPage/home-two";
import Services from "../components/Services";
import BrandLogo from "../components/BrandLogo";
import Funfact from "../components/Funfact";
import CallToAction from "../components/CallToAction";
import Footer from "../components/Footer";
import LoginRegister from "../components/LoginRegister";
import MobileMenu from "../components/MobileMenu";
import Features from "../components/Features";
import Testimonial from "../components/Testimonials/home-two";
import Team from "../components/Team/home-two";

import ServiceThumb from '../assets/img/about.jpg'

const PageLandingPage = () => {
    return (
        <Fragment>
            <Header/>
            <PageHeader
                bgImg={require('../assets/img/landing.jpg')}
                title="Commodoro"
                content= {<h3 className="text-landing"> Welcome to the largest network of coffee farmers </h3>}
            />
            <LandingPage
                // title={'Our Team'}
                // heading="Meet Our <br/> Expert Member"
                thumb={ServiceThumb}
                // content="<b>Businex</b> always try to provide the best Business Solutions for Clinets to grow up their Business very sharply and smoothly. We voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt."
            />
            <Services/>
            <Features classes={'sm-top'}/>
            <Testimonial/>
            <Team/>
            {/* <BrandLogo/>
            <Funfact classes="sp-top"/> */}
            <CallToAction/>
            <Footer/>
            <LoginRegister/>
            <MobileMenu/>
        </Fragment>
    );
};

export default PageLandingPage;