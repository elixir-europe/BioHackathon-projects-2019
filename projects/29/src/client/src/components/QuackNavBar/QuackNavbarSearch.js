import React from 'react';
import styled from 'styled-components';

const Input = styled.input`
    margin-top: 0.7rem;
    margin-left: 1.5rem;
    width: 400px;
    outline: 0;
    border-width: 0 0 0px;
    border-color: black;
    font-family: Dosis;
    font-size: 2rem;
    background-color : #FFFFE0;
    padding-left: 1rem; 

`
const QuackNavbarSearch = () => {
    return (
        <div>
            <Input placeholder="type your query" type="search"/>
        </div>
    );
};

export default QuackNavbarSearch;