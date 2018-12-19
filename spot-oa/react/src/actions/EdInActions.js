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

import SpotActions from './SpotActions'

var SpotDispatcher = require('../dispatchers/SpotDispatcher');
var SpotConstants = require('../constants/SpotConstants');
var SpotUtils = require('../utils/SpotUtils');

class EdInActions {
  static setFilter(filter)
  {
    SpotUtils.setUrlParam('filter', filter);

    SpotDispatcher.dispatch({
      actionType: SpotConstants.UPDATE_FILTER,
      filter: filter
    });
  }

  static reloadSuspicious() {
    SpotActions.toggleMode(SpotConstants.DETAILS_PANEL, SpotConstants.DETAILS_MODE);
    SpotDispatcher.dispatch({
      actionType: SpotConstants.RELOAD_SUSPICIOUS
    });
  }

  static reloadDetails() {
    SpotDispatcher.dispatch({
      actionType: SpotConstants.RELOAD_DETAILS
    });
  }

  static reloadVisualDetails() {
    SpotDispatcher.dispatch({
      actionType: SpotConstants.RELOAD_DETAILS_VISUAL
    });
  }

  static highlightThreat(id)
  {
    SpotDispatcher.dispatch({
      actionType: SpotConstants.HIGHLIGHT_THREAT,
      threat: id
    });
  }

  static unhighlightThreat()
  {
    SpotDispatcher.dispatch({
      actionType: SpotConstants.UNHIGHLIGHT_THREAT
    });
  }

  static selectThreat(threat)
  {
    SpotDispatcher.dispatch({
      actionType: SpotConstants.SELECT_THREAT,
      threat: threat
    });
  }

  static selectIp(ip)
  {
    SpotDispatcher.dispatch({
      actionType: SpotConstants.SELECT_IP,
      ip: ip
    });
  }

  static saveScoring(scoredEmelents) {
    SpotDispatcher.dispatch({
      actionType: SpotConstants.SAVE_SCORED_ELEMENTS,
      scoredElems: scoredEmelents
    });
  }

  static resetScoring(date) {
    SpotDispatcher.dispatch({
      actionType: SpotConstants.RESET_SCORED_ELEMENTS,
      date: date
    });
  }

  static setClassWidth() {
    SpotDispatcher.dispatch({
      actionType: SpotConstants.CHANGE_CSS_CLS
    });
  }
};

export {EdInActions as default}
