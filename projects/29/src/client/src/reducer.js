const SET_RESULTS = 'SET_RESULTS';
const SET_QUERY = 'SET_QUERY';
const SET_EXPRESSIONS = 'SET_EXPRESSIONS';
const SET_VOTESTATE = 'SET_VOTESTATE';
const SET_INDEX = 'SET_INDEX';
const DELETE_SEARCH = 'DELETE_SEARCH'
const DELETE_ALL = 'DELETE_ALL';
const ADD_HAPPY = 'ADD_HAPPY';
const ADD_SAD = 'ADD_SAD';
const SET_INRESULTS = 'SET_INRESULTS'

function reducer(state, action) {
    switch (action.type) {
        case DELETE_ALL: {
            return {
                ...state,
                results: [],
                query: '',
                happy: [],
                sad: [],
                expressions: [],
                happyState: false,
                sadState: false,
                inResults: false
            }
        }
        case SET_INRESULTS: {
            return {
                ...state,
                inResults: true
            }
        }
        case SET_RESULTS: {
            return {
                ...state,
                results: action.data,
                index: action.data.length - 1
            }
        }
        case SET_VOTESTATE: {
            return {
                ...state,
                sadState: action.data === -1,
                happyState: action.data === 1,
            }
        }
        case SET_QUERY: {
            return {
                ...state,
                query: action.data
            }
        }
        case SET_EXPRESSIONS: {
            return {
                ...state,
                expressions: action.data
            }
        }
        case DELETE_SEARCH: {
            return {
                ...state,
                results: [],
                query: ''
            }
        }

        case ADD_HAPPY: {
            let happyElement = state.results.filter((ele) => ele.id === action.data.id)

            let newHappy = [...state.happy, ...happyElement]
            //let newResults = state.results.filter((ele)=>ele.id !== action.data.id)
            //console.log('IN ADD HAPPY', happyElement, newHappy)
            return {
                ...state,
                happy: newHappy,
                index: state.index - 1
            }
        }
        case ADD_SAD: {
            let sadElement = state.results.filter((ele) => ele.id === action.data.id)
            let newSad = [...state.sad, ...sadElement]
            //let newResults = state.results.filter((ele)=>ele.id !== action.data.id)
            return {
                ...state,
                sad: newSad,
                index: state.index - 1

            }
        }


        default:
            return state
    }
}

export default reducer;
