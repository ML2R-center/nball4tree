import decimal

L0 = decimal.Decimal(1e+100)
R0 = decimal.Decimal(1e-200)
cgap = decimal.Decimal(0.0001)
addDim = [512, 512, -512, -512, -512, -512, -512, -512, -512, -512, -512, -512, -512, -512, -512, -512, -512, -512,
          -512, -512, -512, -512, -512, -512, -512, -512, -512, -512, -512, -512, -512, -512, -512, -512, -512, -512,
          -512, -512, -512, -512, -512, -512, -512, -512, -512, -512, -512, -512, -512, -512, -512, -512, -512, -512,
          -512, -512, -512, -512, -512, -512, -512, -512, -512, -512, -512, -512, -512, -512, -512, -512, -512, -512,
          -512, -512, -512, -512, -512, -512, -512, -512, -512, -512, -512, -512, -512, -512, -512, -512, -512, -512,
          -512, -512, -512, -512, -512, -512, -512, -512, -512, -512, -512, -512, -512, -512, -512, -512, -512, -512,
          -512, -512, -512, -512, -512, -512, -512, -512, -512, -512, -512, -512, -512, -512, -512, -512, -512, -512,
          -512, -512, -512, -512]

INIT_RATIO_W2V = 100
INIT_INC_CATCODE = 10

# xalpha = decimal.Decimal(0.2)
xalpha = 'alpha/25'
hrate = 0.1
MAXBETA = 0.999
DIM = 100
DECIMAL_PRECISION = 500

ForestRootsStr = "despair.v.01 take.v.20 splash.v.07 adjourn.v.02 diverge.v.03 unleash.v.01 rest.v.11 leak.v.04 percolate.v.04 delight.v.02 indulge.v.01 analyze.v.02 spell.v.03 free.v.07 freeze.v.01 kill.v.10 enjoy.v.01 exceed.v.01 conceal.v.02 abolish.v.01 obviate.v.01 madden.v.01 absorb.v.04 arm.v.01 settle.v.04 disengage.v.01 discover.v.07 absorb.v.06 sulk.v.01 offer.v.07 fly.v.05 predominate.v.01 cheer.v.03 neglect.v.03 avoid.v.03 blind.v.01 overlay.v.01 settle.v.21 laugh.v.01 address.v.02 save.v.05 err.v.01 campaign.v.03 conform.v.01 make.v.01 miss.v.01 hesitate.v.01 smell.v.02 refuse.v.02 save.v.04 wait.v.01 discharge.v.10 demolish.v.03 exist.v.02 break.v.46 discourage.v.02 prod.v.02 leave.v.12 connect.v.03 dishonor.v.01 reflect.v.03 exempt.v.01 radiate.v.05 fear.v.02 know.v.03 uncover.v.02 converge.v.01 move.v.04 dislike.v.01 beat.v.02 cry.v.02 begin.v.02 forget.v.02 persist.v.03 taste.v.01 rear.v.02 hold.v.02 abandon.v.02 idle.v.02 waive.v.01 rest.v.03 spot.v.02 leave.v.02 neglect.v.01 start.v.08 enter.v.02 season.v.01 guide.v.05 agree.v.07 collapse.v.05 stop.v.01 precipitate.v.03 collide.v.02 be.v.08 open.v.01 satisfy.v.02 blow.v.02 hide.v.02 save.v.03 close.v.01 breathe.v.01 submit.v.03 oppress.v.01 watch.v.05 discard.v.01 worry.v.01 abstain.v.02 play.v.26 avoid.v.01 disagree.v.01 understand.v.02 succeed.v.02 hide.v.01 differ.v.01 remember.v.03 let.v.01 take.v.21 range.v.03 hold.v.10 hang.v.01 lose.v.02 discontinue.v.01 separate.v.08 separate.v.07 sit.v.01 lie.v.02 meet.v.01 shine.v.02 sound.v.02 produce.v.06 burn.v.05 charge.v.02 prevent.v.01 correspond.v.03 love.v.01 like.v.02 look.v.01 learn.v.01 observe.v.06 remember.v.02 exercise.v.04 learn.v.04 determine.v.08 rid.v.01 affirm.v.03 hire.v.01 ache.v.03 emit.v.02 switch.v.03 fail.v.01 free.v.06 give.v.01 confine.v.05 cultivate.v.01 meet.v.10 issue.v.04 fall.v.17 yield.v.12 fail.v.02 fire.v.02 live.v.02 change.v.03 account.v.02 pronounce.v.01 install.v.02 gather.v.01 establish.v.08 create.v.02 know.v.02 intend.v.01 remind.v.01 take.v.08 treat.v.03 move.v.15 begin.v.03 free.v.01 pass.v.22 appear.v.05 miss.v.06 search.v.01 expect.v.03 keep.v.01 practice.v.04 produce.v.02 spread.v.01 sound.v.03 dissemble.v.03 sound.v.06 act.v.08 agree.v.01 lead.v.01 appear.v.02 show.v.04 function.v.01 arrive.v.01 stop.v.05 refer.v.02 prevent.v.02 exist.v.01 include.v.01 feel.v.01 remove.v.01 complain.v.01 beat.v.01 receive.v.05 travel.v.03 watch.v.01 learn.v.02 open.v.02 cover.v.01 touch.v.05 remember.v.01 know.v.01 study.v.02 determine.v.01 examine.v.02 disappear.v.01 end.v.01 excel.v.01 lose.v.05 have.v.09 refrain.v.01 trade.v.01 assail.v.01 win.v.01 necessitate.v.01 have.v.01 work.v.02 designate.v.01 destroy.v.02 affect.v.05 displease.v.01 enter.v.01 perceive.v.01 take.v.04 punish.v.01 accommodate.v.04 meet.v.02 attract.v.02 sensitize.v.02 use.v.01 unmake.v.01 determine.v.03 understand.v.01 leave.v.01 move.v.03 forget.v.01 comfort.v.01 analyze.v.01 work.v.01 kill.v.01 confirm.v.01 compete.v.01 transfer.v.05 contend.v.06 touch.v.01 consume.v.02 support.v.01 desire.v.01 guarantee.v.02 induce.v.02 reach.v.01 amount.v.01 exhaust.v.05 assemble.v.03 appoint.v.02 act.v.02 perform.v.01 become.v.03 succeed.v.01 constitute.v.01 join.v.01 mean.v.03 travel.v.01 spend.v.01 equal.v.01 happen.v.01 remove.v.02 be.v.03 give.v.08 decide.v.01 connect.v.01 make.v.03 gain.v.05 get.v.01 control.v.01 change.v.01 change.v.02 utter.v.02 move.v.02 have.v.02 think.v.03 insist.v.01 express.v.02 be.v.01 use.v.03 act.v.01 entity.n.01"