//
// Licensed to the Apache Software Foundation (ASF) under one or more
// contributor license agreements.  See the NOTICE file distributed with
// this work for additional information regarding copyright ownership.
// The ASF licenses this file to You under the Apache License, Version 2.0
// (the "License"); you may not use this file except in compliance with
// the License.  You may obtain a copy of the License at
//
//    http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
//

import React from 'react'

var EdInActions = require('../../../actions/EdInActions');
var SuspiciousStore = require('../stores/SuspiciousStore');
var SpotUtils = require('../../../utils/SpotUtils');

export default class FilterInput {
  getInitialState()
  {
    return {filter: ''};
  }
  componentDidMount() {
    SuspiciousStore.addChangeFilterListener(this._onFilterChange);
  }
  componentWillUnmount() {
    SuspiciousStore.removeChangeFilterListener(this._onFilterChange);
  }
  render()
  {
    var cssClasses;

    cssClasses = 'form-control';

    if (this.state.filter && !SpotUtils.IP_V4_REGEX.test(this.state.filter))
    {
      cssClasses += ' has-error';
    }

    return (
      <input id={this.props.id} type="text" className={cssClasses} placeholder="0.0.0.0" autoFocus={true} onChange={this._onChange} value={this.state.filter} onKeyUp={this._onKeyUp} />
    );
  }
  _onKeyUp(e)
  {
    if (e.which==13) {
      EdInActions.reloadSuspicious();
    }
  }
  _onChange(e)
  {
    EdInActions.setFilter(e.target.value);
    this.setState({filter: e.target.value});
  }
  _onFilterChange()
  {
    this.setState({filter: SuspiciousStore.getFilter()});
  }
};
