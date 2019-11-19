import React from 'react';
import {QuackLogo} from "../components/QuackLogo";
import {QuackInput} from "../components/QuackInput";
import styled from 'styled-components';

const VerticalWrapper = styled.div`
    display: flex;
    flex-direction: column;
    align-items: center;
`


function QuackSearch(props) {
    return (
        <VerticalWrapper>
            <QuackLogo/>
            <QuackInput/>
        </VerticalWrapper>
    );
}

export default QuackSearch;